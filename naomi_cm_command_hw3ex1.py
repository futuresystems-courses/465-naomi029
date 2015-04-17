which python
python --version
virtualenv -p /usr/bin/python ~/ENV
source $HOME/ENV/bin/activate
pip install cmd3
pip --trusted pypi.python.org install cloudmesh_base
pip --trusted pypi.python.org install cmd3
cm help
cm-generate-command
cm-generate-command naomicommand --path=~
cd cloudmesh_naomicommand/
python setup.py install
cd ~/.cloudmesh/cmd3.yaml #edit file to include command, under modules: "- cloudmesh_naomicommand.plugins"
cm naomicommand
