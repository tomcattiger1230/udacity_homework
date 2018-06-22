(TeX-add-style-hook
 "final_paper"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
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
    "sec:org3e7dc3d"
    "sec:orgad1c2c2"
    "fig:lenet5"
    "fig:inceptionV3"
    "fig:inceptionV4"
    "sec:org210ab0e"
    "sec:org97a1c93"
    "fig:keras"
    "fig:remove"
    "fig:miss1"
    "fig:miss2"
    "fig:missfigure"
    "sec:org4a2437e"
    "fig:imgaug"
    "fig:cat1"
    "fig:cat2"
    "fig:cat3"
    "fig:cat4"
    "fig:cat5"
    "fig:cat6"
    "fig:cats"
    "sec:orgec56f37"
    "fig:selfmodel"
    "sec:orgf7613d4"
    "sec:org8cf7f8d"
    "sec:org2f091fa"
    "fig:kaggle"
    "fig:tb1"
    "fig:tb2"
    "fig:tb3"
    "fig:tb4"
    "fig:tb"
    "sec:org5dd7fe9"
    "fig:hm"
    "sec:org673c358"
    "sec:org5ec6905")
   (LaTeX-add-bibliographies
    "../../../../LibData/Bibliography/bib"))
 :latex)

