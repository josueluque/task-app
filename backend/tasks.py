from invoke import task

# @task
# def app(ctx):
#     ctx.run("python app.py")

@task
def env(ctx):   # 'ctx' convención comúnmente utilizada en Invoke para referirse al contexto de ejecución de tareas. 
    ctx.run("python config/fs.py")

@task
def dependencies(ctx):
    ctx.run("pip install -r requirements.txt")