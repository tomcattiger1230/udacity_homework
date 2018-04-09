(TeX-add-style-hook
 "proposal"
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
    "sec:org9e456b5"
    "sec:org6f63352"
    "sec:org9cf5769"
    "sec:orgd80bbcc"
    "sec:orgef49ea3"
    "sec:org78a5802"
    "sec:orgc29b8e9"
    "sec:org454f235"
    "eq:crossE"
    "eq:lossF"
    "eq:kaggelE"
    "sec:orgd7a83e8"
    "sec:org98086fe"
    "sec:orga35ff75"
    "sec:orga912f23"
    "sec:org6d2ebe4"
    "sec:org4778596")
   (LaTeX-add-bibliographies
    "../../../../LibData/Bibliography/bib"))
 :latex)

