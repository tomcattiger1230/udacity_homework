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
    "sec:org9b67672"
    "sec:orgba8b7f1"
    "fig:lenet5"
    "fig:inceptionV3"
    "fig:inceptionV4"
    "sec:org544440e"
    "sec:orged867fd"
    "fig:keras"
    "fig:remove"
    "fig:miss1"
    "fig:miss2"
    "fig:missfigure"
    "sec:org7d9b262"
    "fig:imgaug"
    "fig:cat1"
    "fig:cat2"
    "fig:cat3"
    "fig:cat4"
    "fig:cat5"
    "fig:cat6"
    "fig:cats"
    "sec:org7de32bb"
    "fig:selfmodel"
    "sec:orgc6cef30"
    "sec:orge8415af"
    "sec:org634f99b"
    "fig:kaggle"
    "fig:tb1"
    "fig:tb2"
    "fig:tb3"
    "fig:tb4"
    "fig:tb"
    "sec:orgccdbc0b"
    "fig:hm"
    "sec:org1aac7ad"
    "sec:org417ee14")
   (LaTeX-add-bibliographies
    "../../../../LibData/Bibliography/bib"))
 :latex)

