(TeX-add-style-hook
 "final_paper"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "ctex")
   (LaTeX-add-labels
    "sec:org5b7cecf"
    "sec:orgf8b2730"
    "sec:org59f6c32"
    "fig:keras"
    "fig:remove"
    "fig:miss1"
    "fig:miss2"
    "fig:missfigure"
    "sec:orgf6aef71"
    "fig:imgaug"
    "fig:cat1"
    "fig:cat2"
    "fig:cat3"
    "fig:cat4"
    "fig:cat5"
    "fig:cat6"
    "fig:cats"
    "sec:org59c1e6b"
    "fig:selfmodel"
    "sec:org9685cf3"
    "sec:org32561f6"
    "sec:org59eb413"
    "fig:kaggle"
    "fig:tb1"
    "fig:tb2"
    "fig:tb3"
    "fig:tb4"
    "fig:tb"
    "sec:orge6b2499"
    "fig:hm"
    "sec:org77d173e"
    "sec:org9417558"))
 :latex)

