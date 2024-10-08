"""The FEM Module"""

### Forms and bases
from .integrator import *
from .bilinear_form import BilinearForm
from .linear_form import LinearForm
from .semilinear_form import SemilinearForm

### Cell Operator
from .scalar_diffusion_integrator import ScalarDiffusionIntegrator
from .scalar_mass_integrator import ScalarMassIntegrator
from .scalar_convection_integrator import ScalarConvectionIntegrator
from .linear_elasticity_integrator import LinearElasticityIntegrator
from .press_work_integrator import PressWorkIntegrator, PressWorkIntegrator1

### Cell Source
from .scalar_source_integrator import ScalarSourceIntegrator
from .vector_source_integrator import VectorSourceIntegrator

### Face Operator
from .scalar_neumann_bc_integrator import ScalarNeumannBCIntegrator

### Face Source

### Dirichlet BC
from .dirichlet_bc import DirichletBC
