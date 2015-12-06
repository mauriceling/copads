epydoc --verbose \
       --pdf \
       --output=doc/epydoc \
       --name="COPADS: Collection of Python Algorithms and Data Structures" \
       --url=https://github.com/mauriceling/copads \
       --show-imports \
       --show-private \
       --show-sourcecode \
       --show-frames \
       --navlink=https://github.com/mauriceling/copads \
       copads

mv doc/epydoc/api.pdf doc/COPADS_API_Documentation.pdf
rm -rf doc/epydoc

epydoc --verbose \
       --html \
       --output=doc/epydoc \
       --name="COPADS: Collection of Python Algorithms and Data Structures" \
       --url=https://github.com/mauriceling/copads \
       --show-imports \
       --show-private \
       --show-sourcecode \
       --show-frames \
       --navlink=https://github.com/mauriceling/copads \
       copads
