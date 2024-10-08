
import argparse

from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

from fealpy.experimental import logger
logger.setLevel('WARNING')
from fealpy.experimental.backend import backend_manager as bm
from fealpy.experimental.mesh import TriangleMesh
from fealpy.experimental.functionspace import LagrangeFESpace
from fealpy.experimental.fem import SemilinearForm
from fealpy.experimental.fem import ScalarDiffusionIntegrator, ScalarMassIntegrator
from fealpy.experimental.fem import ScalarSourceIntegrator
from fealpy.experimental.pde.semilinear_2d import SemilinearData
from fealpy.utils import timer
from fealpy.decorator import barycentric


## 参数解析
parser = argparse.ArgumentParser(description=
        """
        任意次有限元方法求解possion方程
        """)

parser.add_argument('--degree',
        default=1, type=int,
        help='Lagrange 有限元空间的次数, 默认为 1 次.')

parser.add_argument('--n',
        default=4, type=int,
        help='初始网格剖分段数.')

parser.add_argument('--maxit',
        default=4, type=int,
        help='默认网格加密求解的次数, 默认加密求解 4 次')

parser.add_argument('--backend',
        default='pytorch', type=str,
        help='默认后端为numpy')

parser.add_argument('--meshtype',
        default='tri', type=str,
        help='默认网格为三角形网格')

args = parser.parse_args()


bm.set_backend(args.backend)
p = args.degree
n = args.n
meshtype = args.meshtype
maxit = args.maxit

tmr = timer()
next(tmr)

domain = [0, 1, 0, 2]
nx = 4
ny = 4
pde = SemilinearData(domain)
mesh = TriangleMesh.from_box(domain, nx=nx, ny=ny)

p = 1
maxit = 8
tol = 1e-8
NDof = bm.zeros(maxit, dtype=bm.int64)
errorMatrix = bm.zeros((2, maxit), dtype=bm.float64)
tmr.send('网格和pde生成时间')
errorType = ['$|| u - u_h||_{\Omega, 0}$', '$||\\nabla u - \\nabla u_h||_{\Omega, 0}$']
def func(u):
    return u**3

def grad_func(u):
    return 3*u**2

def diffusion_coef(p):
    return pde.diffusion_coefficient(p)

def reaction_coef(p):
    return pde.reaction_coefficient(p)

reaction_coef.func = func
reaction_coef.grad_func = grad_func
    
for i in range(maxit):
    #定义函数空间
    space = LagrangeFESpace(mesh, p=p)
    NDof[i] = space.number_of_global_dofs()
    tmr.send(f'第{i}次空间时间')

    u0 = space.function()
    du = space.function()
    diffusion_coef.uh = u0
    reaction_coef.uh = u0
    isDDof = space.set_dirichlet_bc(pde.dirichlet, u0)
    isIDof = ~isDDof

    #定义积分子
    D = ScalarDiffusionIntegrator(diffusion_coef, q=p+2, method='semilinear')
    M = ScalarMassIntegrator(reaction_coef, q=p+2, method='semilinear')
    f = ScalarSourceIntegrator(pde.source, q=p+2)

    while True:
        #矩阵组装
        n = SemilinearForm(space)
        n.add_integrator([D, M])
        n.add_integrator(f)
        A, F = n.assembly()
        tmr.send(f'第{i}次矩组装时间')
        
        #求解增量
        A = csr_matrix((A.values(), A.indices()), A.shape)
        du[isIDof] = bm.tensor(spsolve(A[isIDof, :][:, isIDof], F[isIDof]).reshape(-1), dtype=du[isIDof].dtype)
        u0 += du
        tmr.send(f'第{i}次求解器时间')

        #清除积分子缓存
        D.clear()
        M.clear()

        #计算误差
        err = bm.max(bm.abs(du.array))
        if err < tol:
            break

    @barycentric
    def ugval(p):
        return space.grad_value(u0, p)

    errorMatrix[0, i] = mesh.error(pde.solution, u0, q=p+2)
    errorMatrix[1, i] = mesh.error(pde.gradient, ugval, q=p+2)
    if i < maxit-1:
        mesh.uniform_refine()
    tmr.send(f'第{i}次误差计算及网格加密时间')

next(tmr)
print(NDof)
print(errorMatrix)
print(errorMatrix[:, 0:-1]/errorMatrix[:, 1:])
