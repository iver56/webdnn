from webdnn.backend.fallback.kernels.elementwise import register_elementwise_kernel
from webdnn.graph.operators.sin import Sin

register_elementwise_kernel(Sin, "y = Math.sin(x0);")
