import numpy as np
from fealpy.decorator import cartesian
from fealpy.experimental.backend import backend_manager as bm
triangle_mesh_one_box = [
        {
            ##input
            "bcs" : np.array([[0, 0, 1], [0, 1, 0], [1/3, 1/3, 1/3]], dtype=np.float64),


            ##result
            "number_of_local_dofs": 6,
            "number_of_global_dofs": 9,
            "interpolation points":np.array(
                                 [[0., 0.],
                                 [0., 1.],
                                 [1., 0.],
                                 [1., 1.],
                                 [0. , 0.5],
                                 [0.5, 0. ],
                                 [0.5, 0.5],
                                 [0.5, 1. ],
                                 [1. , 0.5]], dtype=np.float64), 
            "cell_to_dof":np.array([
                                 [2, 8, 5, 3, 6, 0],
                                 [1, 4, 7, 0, 6, 3]], dtype=np.int32),
            "face_to_dof":np.array(
                                 [[1, 4, 0],
                                 [0, 5, 2],
                                 [3, 6, 0],
                                 [3, 7, 1],
                                 [2, 8, 3]], dtype=np.int32),
            "edge_to_dof":np.array(
                                 [[1, 4, 0],
                                 [0, 5, 2],
                                 [3, 6, 0],
                                 [3, 7, 1],
                                 [2, 8, 3]], dtype=np.int32),
            "is_boundary_dof":np.array(
                                [ True,  True,  True,  True , 
                                True , True ,False , True , True], dtype=np.bool),
            "geo_dimension":2,
            "top_dimension":2,
            "basis":np.array(
                    [[[-0., 0., 0., -0., 0., 1.],
                     [-0., 0., 0., 1., 0., -0.],
                     [-0.11111111, 0.44444444, 0.44444444, 
                    -0.11111111, 0.44444444, -0.11111111]]],dtype = np.float64),
            "grad_basis":np.array([[[[-1., 1.],
                    [ 0., 0.],
                    [ 4., -4.],
                    [ 0., -1.],
                    [ 0., 4.],
                    [-3., 0.]],

                    [[ 1., -1.],
                    [ 0., 0.],
                    [-4., 4.],
                    [ 0., 1.],
                    [ 0., -4.],
                    [ 3., 0.]]],


                    [[[-1., 1.],
                    [ 4., -4.],
                    [ 0., 0.],
                    [ 0., 3.],
                    [-4., 0.],
                    [ 1., 0.]],

                    [[ 1., -1.],
                    [-4., 4.],
                    [ 0., 0.],
                    [ 0., -3.],
                    [ 4., 0.],
                    [-1., 0.]]],


                    [[[ 0.33333333, -0.33333333],
                    [ 1.33333333, 0.],
                    [ 0., -1.33333333],
                    [ 0., 0.33333333],
                    [-1.33333333, 1.33333333],
                    [-0.33333333, 0.]],

                    [[-0.33333333, 0.33333333],
                    [-1.33333333, 0.],
                    [ 0., 1.33333333],
                    [ 0., -0.33333333],
                    [ 1.33333333, -1.33333333],
                    [ 0.33333333, 0.]]]], dtype=np.float64),

            "interpolate":np.array(
                                 [0 , 0, 0, 0.70807342, 0, 0, 
                                 0.22984885, 0.40342268,0.40342268], dtype=np.float64),
            "value":np.array([[[0,         0.70807342, 0.20277919],
                              [0.70807342, 0.       , 0.20277919]]], np.float64),
                             
            "grad_value":np.array([[[[0,         0.21132197],
                                  [0.69429533,0.51052953],
                                  [0.23143178,0.5424896 ]],

                                 [[0.51052953,0.69429533],
                                  [0.21132197,0.        ],
                                  [0.5424896,0.23143178]]]], dtype=np.float64)
 
        }
        ]
