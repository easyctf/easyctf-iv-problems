import os
import traceback
import sys

import yaml

with open(os.path.join(os.path.dirname(__file__), "services")) as f:
    base = f.read()
with open(os.path.join(os.path.dirname(__file__), "redirect.template")) as f:
    redirect_template = f.read()
with open(os.path.join(os.path.dirname(__file__), "server.template")) as f:
    server_template = f.read()

problem_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
problem_names = os.listdir(problem_dir)

if __name__ == "__main__":
    service = None
    if len(sys.argv) > 1:
        service = sys.argv[1]
    new_services = []
    os.system("rm -f /etc/xinetd.d/easyctf/*")  # probably redo this later
    for name in problem_names:
        if name.startswith("."):
            continue
        if service and name != service:
            continue
        problem_folder = os.path.join(problem_dir, name)
        if not os.path.isdir(problem_folder):
            continue
        try:
            curr = os.getcwd()
            os.chdir(problem_folder)
            files = os.listdir(problem_folder)
            if "problem.yml" not in files:
                continue
            with open(os.path.join(problem_folder, "problem.yml")) as f:
                metadata = yaml.load(f)
            if metadata:
                docker = metadata.get("docker")
                if docker and ("Dockerfile" in files):
                    os.system("docker build -t {} .".format(name))
                    args = docker.get("args", "")
                    os.system("docker rm -f $(docker ps -q --filter='ancestor={name}')".format(name=name))
                    os.system("docker run --detach=true {args} {name}".format(args=args, name=name))
                net = metadata.get("net")
                if net:
                    port = net.get("port")
                    exe = net.get("server")
                    if exe:
                        exe_path = os.path.join(problem_folder, exe)
                        new_services.append("{} {}/tcp".format(name, port))
                        with open("/etc/xinetd.d/easyctf/{}".format(name), "w") as f:
                            f.write(server_template.format(name=name, exe_path=exe_path, port=port))
                        print("installed {}".format(name))
                    redir = net.get("redirect")
                    if redir:
                        new_services.append("{} {}/tcp".format(name, port))
                        with open("/etc/xinetd.d/easyctf/{}".format(name), "w") as f:
                            f.write(redirect_template.format(name=name, redirect=redir, port=port))
                        print("installed {}".format(name))
            os.chdir(curr)
        except:
            traceback.print_exc(file=sys.stderr)

    with open("/etc/services", "w") as f:
        f.write(base + "\n".join(new_services))

    os.system("/etc/init.d/xinetd restart")
