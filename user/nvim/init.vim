let g:python3_host_prog = '/usr/bin/python3'  " dont search, this in the good one
let g:loaded_python_provider = 1              " disables python2

call plug#begin('~/.config/nvim/plugged/')

    " Plug 'terryma/vim-multiple-cursors'
    " Plug 'vim-scripts/argtextobj'
    "Plugin 'nvie/vim-flake8'
    "Plugin 'psf/black'
    "Plugin 'vim-airline/vim-airline'
    Plug 'dense-analysis/ale'
    Plug 'easymotion/vim-easymotion'
    Plug 'heavenshell/vim-pydocstring', {'do': 'make install'}
    Plug 'kana/vim-textobj-entire'
    Plug 'kana/vim-textobj-user'
    Plug 'ludovicchabant/vim-gutentags'
    Plug 'mg979/vim-visual-multi'
    Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
    Plug 'tmhedberg/SimpylFold'
    Plug 'tomasr/molokai'
    Plug 'tpope/vim-commentary'
    Plug 'tpope/vim-repeat'
    Plug 'tpope/vim-surround'
    Plug 'yhat/vim-docstring'
    Plug 'zhimsel/vim-stay'
    Plug 'zxqfl/tabnine-vim'

call plug#end()

source ~/.vimrc.keymaps
source ~/.vimrc.common

" merges upstream python3 path with per-env path
python3 << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    original_path = sys.path
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    exec(open(activate_this).read(), dict(__file__=activate_this))
    sys.path.extend(original_path)
EOF
