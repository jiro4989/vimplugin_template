" Vim plugin for description
" Last Change: $CURRENT_DATE
" Maintainer:  Jiro <jiroron666@gmail.com>
" License:     This file is placed in the public domain.

if exists("g:loaded_$PLUGIN_NAME")
  finish
endif
let g:loaded_$PLUGIN_NAME = 1

let s:save_cpo = &cpo
set cpo&vim

if !exists(":$COMMAND_NAME")
  command! -nargs=0 $COMMAND_NAME call $PLUGIN_NAME#$FUNC_NAME()
  nnoremap X :$COMMAND_NAME<CR>
endif

let &cpo = s:save_cpo
unlet s:save_cpo
