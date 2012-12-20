if has("autocmd")
  augroup autoinsert
    au!
    autocmd BufNewFile *.c call s:Template("c")
    autocmd BufNewFile *.cpp call s:Template("cpp")
  augroup END
  endif
  function s:Template(argument)
          if (a:argument == "help")
                  echo "Currently available templates:"
                  echo " py          - Python"
                  echo " sh          - Shell Script"
          else
                  " First delete all in the current buffer
                  %d

                  " Stuff for plain C
                  if (a:argument == "c")
                          0r ~/.vim/skeletons/template.py
                          set ft=python
                        elseif (a:argument == "cpp")
                          0r ~/.vim/skeletons/template.sh
                          set ft=sh
                  endif
          endif
  endfunction

  command! -nargs=1 Template call s:Template(<f-args>)
