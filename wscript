import os
from waflib import TaskGen

def options(opt):
    opt.add_option('--prefix', dest='prefix', default=os.getcwd() + '/dist', help='installation prefix')

def configure(conf):
    conf.env.AS = 'clang'
    conf.env.STRIP = 'strip'
    conf.env.PREFIX = conf.options.prefix
    conf.msg('Ready for deployment', 'YES (ABSOLUTELY)')

def build(bld):
    target_app = bld(
        rule    = '${AS} -nostdlib -static ${SRC} -o ${TGT}',
        source  = 'main.s',
        target  = 'bin_amnsnnnnnnnnnnnnnaaagay',
        install_path = '${PREFIX}/bin'
    )

    if bld.cmd == 'build':
        bld.add_post_fun(lambda bld: os.system(f"{bld.env.STRIP} build/abstract_beast"))

TaskGen.declare_chain(
    name    = 'assemble',
    rule    = '${AS} -c ${SRC} -o ${TGT}',
    ext_in  = '.s',
    ext_out = '.o'
)