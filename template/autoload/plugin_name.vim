let s:save_cpo = &cpo
set cpo&vim

function! $PLUGIN_NAME#$FUNC_NAME()
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
