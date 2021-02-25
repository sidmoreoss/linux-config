if has('python3')
endif
syntax on
" inoremap {<CR> {<CR>}<Esc>ko
set noshowmatch
set relativenumber
set nohlsearch
set hidden
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.config/nvim/undodir
set undofile
set incsearch
call plug#begin('~/.config/nvim/plugged')
Plug 'mattn/emmet-vim'
Plug 'mizuchi/stl-syntax'
Plug 'scrooloose/nerdtree'
Plug 'scrooloose/syntastic'
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'tweekmonster/gofmt.vim'
Plug 'tpope/vim-fugitive'
Plug 'vim-utils/vim-man'
Plug 'mbbill/undotree'
Plug 'sheerun/vim-polyglot'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'lyuts/vim-rtags'
Plug 'jremmen/vim-ripgrep'
Plug 'prettier/vim-prettier', { 'do': 'npm install' }
Plug 'tpope/vim-surround'
Plug 'jiangmiao/auto-pairs'
Plug 'dylanaraps/wal.vim'
Plug 'davidhalter/jedi-vim'
" call PlugInstall to install plugins
call plug#end()
colorscheme wal
set background=dark
set clipboard=unnamedplus
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
" let g:prettier#autoformat = 1
