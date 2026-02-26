from waflib import TaskGen

def options(opt):
    pass

def configure(conf):
    # 在 Termux 环境下，直接指定 clang
    conf.env.AS = 'clang'
    conf.env.LD = 'clang'
    conf.msg('Checking for Gayness level', 'EXTREME')

def build(bld):
    # 核心：手动创建一个任务，告诉 Waf 如何处理 .s 文件
    bld(
        rule   = '${AS} -nostdlib -static ${SRC} -o ${TGT}',
        source = 'main.s',
        target = 'main',
        shell  = True
    )

# 强制映射后缀（这就是解决你那个报错的关键）
TaskGen.declare_chain(
    name    = 'assemble',
    rule    = '${AS} -c ${SRC} -o ${TGT}',
    shell   = True,
    ext_in  = '.s',
    ext_out = '.o',
    reentrant = False
)