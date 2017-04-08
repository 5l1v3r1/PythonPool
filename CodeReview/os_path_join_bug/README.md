


os.path.join(path, *paths) 方法

该方法目的是使用 一个或多个 路径名 拼接起来,问题是 当 *paths 中有绝对路径时,会覆盖 path 的路径.

Demo 1: 链接相对路径

    os.path.join('/var/www/html/', 'plulic')

    输出:

    /var/www/html//plulic

Demo 1: 链接绝对路径

    os.path.join('/var/www/html/', '/etc/passwd')

    输出:

    /etc/passwd