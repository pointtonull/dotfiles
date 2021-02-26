let g:python3_host_prog = '/usr/bin/python3'  " dont search, this in the good one
let g:loaded_python_provider = 1              " disables python2

call plug#begin('~/.config/nvim/plugged/')
    " Plug 'cloudhead/neovim-fuzzy'
    " Plug 'felixhummel/setcolors.vim'
    " Plug 'heavenshell/vim-pydocstring', {'do': 'make install'}
    " Plug 'mhinz/vim-signify' " vim-gitgutter
    " Plug 'neovim/nvim-lspconfig'
    " Plug 'psf/black'
    " Plug 'psf/black', { 'branch': 'stable' }
    " Plug 'rafi/awesome-vim-colorschemes'
    " Plug 'tpope/vim-fugitive'
    " Plug 'vim-airline/vim-airline'
    " Plug 'vim-scripts/ShowMarks'  " working with problems
    " Plug 'vim-scripts/argtextobj.vim'
    Plug 'airblade/vim-gitgutter', { 'do': ':helptags doc' }
    Plug 'dense-analysis/ale'
    Plug 'drewtempelmeyer/palenight.vim'
    Plug 'easymotion/vim-easymotion'
    Plug 'glacambre/firenvim', { 'do': { _ -> firenvim#install(0) } }
    Plug 'glts/vim-textobj-comment'
    Plug 'honza/vim-snippets'
    Plug 'jeetsukumaran/vim-pythonsense'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'kana/vim-textobj-diff'
    Plug 'kana/vim-textobj-entire'
    Plug 'kana/vim-textobj-indent'
    Plug 'kana/vim-textobj-user'
    Plug 'kshenoy/vim-signature'
    Plug 'kyoz/purify', { 'rtp': 'vim' }
    Plug 'ludovicchabant/vim-gutentags'
    Plug 'mg979/vim-visual-multi'
    Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
    Plug 'nvie/vim-flake8'
    Plug 'sainnhe/sonokai'
    Plug 'sheerun/vim-polyglot'
    Plug 'sirver/UltiSnips'
    Plug 'tmhedberg/SimpylFold'
    Plug 'tomasr/molokai'
    Plug 'tpope/vim-commentary'
    Plug 'tpope/vim-repeat'
    Plug 'tpope/vim-rhubarb'
    Plug 'tpope/vim-surround'
    Plug 'vim-scripts/indentpython.vim'
    Plug 'wellle/targets.vim'
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

" lua <<EOF
" require'lspconfig'.pyls.setup{}
" EOF
" set completeopt-=preview
" " use omni completion provided by lsp
" autocmd Filetype python setlocal omnifunc=v:lua.vim.lsp.omnifunc
