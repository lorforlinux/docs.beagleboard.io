#!/bin/bash
docker run --rm -it -v $(pwd):/build/docs.beagleboard.org:rw beagle/sphinx-build-env /bin/bash
