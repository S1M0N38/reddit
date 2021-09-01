## Configuration file for jupyter-notebook.

## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = "working"

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
#  Default: True
c.NotebookApp.open_browser = False

## The name of the default kernel to start
#  Default: 'python3'
c.MultiKernelManager.default_kernel_name = "reddit"

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
c.MappingKernelManager.default_kernel_name = "reddit"

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
c.AsyncMultiKernelManager.default_kernel_name = "reddit"

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
c.AsyncMappingKernelManager.default_kernel_name = "reddit"

## The name of the default kernel to start
#  See also: MultiKernelManager.default_kernel_name
c.GatewayKernelManager.default_kernel_name = "reddit"
