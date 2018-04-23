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
    "sec:org964cc8f"
    "sec:org8f0ac97"
    "sec:orgadcee09"
    "sec:orgd93702f"
    "fig:cat1"
    "fig:cat2"
    "fig:cat3"
    "fig:cat4"
    "fig:cat5"
    "fig:cat6"
    "fig:cats"
    "sec:org22eece6"
    "sec:org5109912"
    "sec:orgd4af9e4"
    "sec:org67d22bb"
    "fig:kaggle"
    "sec:org63942ee"))
 :latex)

