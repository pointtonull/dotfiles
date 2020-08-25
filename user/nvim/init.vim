"set runtimepath^=~/.vim runtimepath+=~/.vim/after
"let &packpath = &runtimepath

let g:loaded_python_provider = 1  " disables python2

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
source ~/.vim/plugin/argtextobj.vim

