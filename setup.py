from setuptools import setup

setup(
    name='django-theme-adminlte3',
    version='3.2.0.2',
    url='https://github.com/kelsoncm/django-theme-adminlte3',
    download_url='https://github.com/kelsoncm/django-theme-adminlte3/releases',
    description='Django Admin LTE v3 Theme',
    license="MIT license",
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    keywords=['django', 'admin lte', 'theme'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment ',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
    python_requires='>=3.7',
    install_requires=['Django>=3.2'],
    packages=['adminlte3', 'adminlte3.templatetags', 'adminlte3_admin'],
    package_dir={'adminlte3': 'adminlte3'},
    package_data={'adminlte3_admin': ['templates/*', 'templates/admin_ref/*', 'templates/admin/*', 'templates/admin_ref/user/*', 'templates/admin_ref/widgets/*', 'templates/admin_ref/edit_inline/*', 'templates/admin_ref/includes/*', 'templates/admin/widgets/*', 'templates/admin/includes/*'], 'adminlte3': ['templates/*', 'static/*', 'templates/auth/*', 'templates/registration/*', 'templates/django/*', 'templates/adminlte3/*', 'templates/auth/widgets/*', 'templates/django/forms/*', 'templates/django/forms/widgets/*', 'templates/django/forms/errors/*', 'templates/django/forms/formsets/*', 'templates/django/forms/errors/dict/*', 'templates/django/forms/errors/list/*', 'templates/layouts/*', 'templates/layouts/partials/*', 'static/datatables-colreorder/*', 'static/fontawesome-free/*', 'static/bs-stepper/*', 'static/datatables-fixedcolumns/*', 'static/bootstrap/*', 'static/flot/*', 'static/flag-icon-css/*', 'static/datatables-searchbuilder/*', 'static/datatables-autofill/*', 'static/jszip/*', 'static/fastclick/*', 'static/pace-progress/*', 'static/datatables-buttons/*', 'static/sparklines/*', 'static/datatables-rowreorder/*', 'static/dropzone/*', 'static/daterangepicker/*', 'static/jquery-ui/*', 'static/datatables-select/*', 'static/jqvmap/*', 'static/ekko-lightbox/*', 'static/datatables-bs4/*', 'static/chart.js/*', 'static/jquery/*', 'static/icheck-bootstrap/*', 'static/moment/*', 'static/datatables-keytable/*', 'static/jquery-mousewheel/*', 'static/select2/*', 'static/jquery-mapael/*', 'static/datatables-fixedheader/*', 'static/codemirror/*', 'static/bootstrap-slider/*', 'static/overlayScrollbars/*', 'static/jquery-validation/*', 'static/datatables-scroller/*', 'static/favicon/*', 'static/popper/*', 'static/datatables-responsive/*', 'static/bootstrap-colorpicker/*', 'static/select2-bootstrap4-theme/*', 'static/datatables-rowgroup/*', 'static/fullcalendar/*', 'static/sweetalert2-theme-bootstrap-4/*', 'static/datatables-searchpanes/*', 'static/toastr/*', 'static/datatables/*', 'static/jsgrid/*', 'static/bs-custom-file-input/*', 'static/pdfmake/*', 'static/ion-rangeslider/*', 'static/adminlte3/*', 'static/raphael/*', 'static/uplot/*', 'static/summernote/*', 'static/jquery-knob/*', 'static/filterizr/*', 'static/inputmask/*', 'static/bootstrap4-duallistbox/*', 'static/bootstrap-switch/*', 'static/tempusdominus-bootstrap-4/*', 'static/sweetalert2/*', 'static/datatables-colreorder/css/*', 'static/datatables-colreorder/js/*', 'static/fontawesome-free/css/*', 'static/fontawesome-free/webfonts/*', 'static/bs-stepper/css/*', 'static/bs-stepper/js/*', 'static/datatables-fixedcolumns/css/*', 'static/datatables-fixedcolumns/js/*', 'static/bootstrap/js/*', 'static/flot/plugins/*', 'static/flag-icon-css/css/*', 'static/flag-icon-css/flags/*', 'static/flag-icon-css/flags/1x1/*', 'static/flag-icon-css/flags/4x3/*', 'static/datatables-searchbuilder/css/*', 'static/datatables-searchbuilder/js/*', 'static/datatables-autofill/css/*', 'static/datatables-autofill/js/*', 'static/pace-progress/themes/*', 'static/pace-progress/themes/green/*', 'static/pace-progress/themes/red/*', 'static/pace-progress/themes/blue/*', 'static/pace-progress/themes/white/*', 'static/pace-progress/themes/yellow/*', 'static/pace-progress/themes/black/*', 'static/pace-progress/themes/silver/*', 'static/pace-progress/themes/purple/*', 'static/pace-progress/themes/orange/*', 'static/pace-progress/themes/pink/*', 'static/datatables-buttons/css/*', 'static/datatables-buttons/js/*', 'static/datatables-rowreorder/css/*', 'static/datatables-rowreorder/js/*', 'static/dropzone/min/*', 'static/jquery-ui/images/*', 'static/datatables-select/css/*', 'static/datatables-select/js/*', 'static/jqvmap/maps/*', 'static/jqvmap/maps/continents/*', 'static/datatables-bs4/css/*', 'static/datatables-bs4/js/*', 'static/moment/locale/*', 'static/datatables-keytable/css/*', 'static/datatables-keytable/js/*', 'static/select2/css/*', 'static/select2/js/*', 'static/select2/js/i18n/*', 'static/jquery-mapael/maps/*', 'static/datatables-fixedheader/css/*', 'static/datatables-fixedheader/js/*', 'static/codemirror/theme/*', 'static/codemirror/keymap/*', 'static/codemirror/mode/*', 'static/codemirror/addon/*', 'static/codemirror/mode/wast/*', 'static/codemirror/mode/htmlmixed/*', 'static/codemirror/mode/ntriples/*', 'static/codemirror/mode/yaml/*', 'static/codemirror/mode/markdown/*', 'static/codemirror/mode/fortran/*', 'static/codemirror/mode/gfm/*', 'static/codemirror/mode/sql/*', 'static/codemirror/mode/troff/*', 'static/codemirror/mode/lua/*', 'static/codemirror/mode/python/*', 'static/codemirror/mode/nginx/*', 'static/codemirror/mode/haml/*', 'static/codemirror/mode/vue/*', 'static/codemirror/mode/xquery/*', 'static/codemirror/mode/htmlembedded/*', 'static/codemirror/mode/sas/*', 'static/codemirror/mode/shell/*', 'static/codemirror/mode/css/*', 'static/codemirror/mode/julia/*', 'static/codemirror/mode/smarty/*', 'static/codemirror/mode/haxe/*', 'static/codemirror/mode/xml/*', 'static/codemirror/mode/modelica/*', 'static/codemirror/mode/ecl/*', 'static/codemirror/mode/turtle/*', 'static/codemirror/mode/properties/*', 'static/codemirror/mode/mumps/*', 'static/codemirror/mode/q/*', 'static/codemirror/mode/ttcn/*', 'static/codemirror/mode/soy/*', 'static/codemirror/mode/smalltalk/*', 'static/codemirror/mode/mbox/*', 'static/codemirror/mode/spreadsheet/*', 'static/codemirror/mode/diff/*', 'static/codemirror/mode/vhdl/*', 'static/codemirror/mode/cmake/*', 'static/codemirror/mode/protobuf/*', 'static/codemirror/mode/d/*', 'static/codemirror/mode/fcl/*', 'static/codemirror/mode/pig/*', 'static/codemirror/mode/forth/*', 'static/codemirror/mode/brainfuck/*', 'static/codemirror/mode/gherkin/*', 'static/codemirror/mode/http/*', 'static/codemirror/mode/cobol/*', 'static/codemirror/mode/jinja2/*', 'static/codemirror/mode/rpm/*', 'static/codemirror/mode/ebnf/*', 'static/codemirror/mode/groovy/*', 'static/codemirror/mode/vbscript/*', 'static/codemirror/mode/go/*', 'static/codemirror/mode/textile/*', 'static/codemirror/mode/dockerfile/*', 'static/codemirror/mode/asterisk/*', 'static/codemirror/mode/rst/*', 'static/codemirror/mode/eiffel/*', 'static/codemirror/mode/tiddlywiki/*', 'static/codemirror/mode/apl/*', 'static/codemirror/mode/mllike/*', 'static/codemirror/mode/livescript/*', 'static/codemirror/mode/tornado/*', 'static/codemirror/mode/haskell/*', 'static/codemirror/mode/sparql/*', 'static/codemirror/mode/stylus/*', 'static/codemirror/mode/cypher/*', 'static/codemirror/mode/dart/*', 'static/codemirror/mode/ruby/*', 'static/codemirror/mode/tcl/*', 'static/codemirror/mode/powershell/*', 'static/codemirror/mode/handlebars/*', 'static/codemirror/mode/r/*', 'static/codemirror/mode/sass/*', 'static/codemirror/mode/puppet/*', 'static/codemirror/mode/pegjs/*', 'static/codemirror/mode/gas/*', 'static/codemirror/mode/django/*', 'static/codemirror/mode/webidl/*', 'static/codemirror/mode/octave/*', 'static/codemirror/mode/pug/*', 'static/codemirror/mode/twig/*', 'static/codemirror/mode/nsis/*', 'static/codemirror/mode/asn.1/*', 'static/codemirror/mode/solr/*', 'static/codemirror/mode/perl/*', 'static/codemirror/mode/dylan/*', 'static/codemirror/mode/velocity/*', 'static/codemirror/mode/clike/*', 'static/codemirror/mode/jsx/*', 'static/codemirror/mode/sieve/*', 'static/codemirror/mode/haskell-literate/*', 'static/codemirror/mode/slim/*', 'static/codemirror/mode/elm/*', 'static/codemirror/mode/clojure/*', 'static/codemirror/mode/mirc/*', 'static/codemirror/mode/coffeescript/*', 'static/codemirror/mode/mscgen/*', 'static/codemirror/mode/vb/*', 'static/codemirror/mode/pascal/*', 'static/codemirror/mode/yaml-frontmatter/*', 'static/codemirror/mode/swift/*', 'static/codemirror/mode/z80/*', 'static/codemirror/mode/mathematica/*', 'static/codemirror/mode/tiki/*', 'static/codemirror/mode/erlang/*', 'static/codemirror/mode/asciiarmor/*', 'static/codemirror/mode/crystal/*', 'static/codemirror/mode/toml/*', 'static/codemirror/mode/commonlisp/*', 'static/codemirror/mode/ttcn-cfg/*', 'static/codemirror/mode/php/*', 'static/codemirror/mode/oz/*', 'static/codemirror/mode/dtd/*', 'static/codemirror/mode/idl/*', 'static/codemirror/mode/yacas/*', 'static/codemirror/mode/verilog/*', 'static/codemirror/mode/javascript/*', 'static/codemirror/mode/rust/*', 'static/codemirror/mode/scheme/*', 'static/codemirror/mode/stex/*', 'static/codemirror/mode/factor/*', 'static/codemirror/addon/mode/*', 'static/codemirror/addon/dialog/*', 'static/codemirror/addon/wrap/*', 'static/codemirror/addon/fold/*', 'static/codemirror/addon/display/*', 'static/codemirror/addon/search/*', 'static/codemirror/addon/tern/*', 'static/codemirror/addon/scroll/*', 'static/codemirror/addon/edit/*', 'static/codemirror/addon/merge/*', 'static/codemirror/addon/runmode/*', 'static/codemirror/addon/lint/*', 'static/codemirror/addon/hint/*', 'static/codemirror/addon/selection/*', 'static/codemirror/addon/comment/*', 'static/bootstrap-slider/css/*', 'static/overlayScrollbars/css/*', 'static/overlayScrollbars/js/*', 'static/jquery-validation/localization/*', 'static/datatables-scroller/css/*', 'static/datatables-scroller/js/*', 'static/popper/esm/*', 'static/popper/umd/*', 'static/datatables-responsive/css/*', 'static/datatables-responsive/js/*', 'static/bootstrap-colorpicker/css/*', 'static/bootstrap-colorpicker/js/*', 'static/datatables-rowgroup/css/*', 'static/datatables-rowgroup/js/*', 'static/fullcalendar/locales/*', 'static/datatables-searchpanes/css/*', 'static/datatables-searchpanes/js/*', 'static/jsgrid/i18n/*', 'static/jsgrid/demos/*', 'static/ion-rangeslider/css/*', 'static/ion-rangeslider/js/*', 'static/css/*', 'static/img/*', 'static/js/*', 'static/css/alt/*', 'static/img/credit/*', 'static/js/pages/*', 'static/summernote/lang/*', 'static/summernote/plugin/*', 'static/summernote/font/*', 'static/summernote/plugin/hello/*', 'static/summernote/plugin/specialchars/*', 'static/summernote/plugin/databasic/*', 'static/bootstrap-switch/css/*', 'static/bootstrap-switch/js/*', 'static/bootstrap-switch/css/bootstrap3/*', 'static/bootstrap-switch/css/bootstrap2/*', 'static/tempusdominus-bootstrap-4/css/*', 'static/tempusdominus-bootstrap-4/js/*']},
)
