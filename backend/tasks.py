from invoke import task

@task(name="generate-env")
def generate_env(ctx):   # 'ctx' convención comúnmente utilizada en Invoke para referirse al contexto de ejecución de tareas. 
    ctx.run("python config/genv.py")
