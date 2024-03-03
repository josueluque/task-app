import { useState, useEffect } from "react";
import { createTask, fetchTask, updateTask, deleteTask } from "../../api/tasks";
import { useParams, useNavigate } from "react-router-dom";
// import axios from "axios";

function TaskForm(){
    // Estado local (inicial) para el título y la descripción de la tarea.
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    // Obtiene los parámetros de la URL y la función de navegación
    const params = useParams();
    const navigate = useNavigate();

    // Función que maneja el envío del formulario.
    const handleSubmit = async (e) => {
        e.preventDefault();
        /*
        -- Another form --
        const res = await fetch('http://localhost:8000/task', {
          method: 'POST',
          body: JSON.stringify({
            title,
            description
          }),
          headers: {
            'Content-Type': 'application/json'
          }
        })

        const data = await res.json(); #Convierte los datos a formato json (serailizacion) 
        
        const res = await axios.post('http://localhost:8000/task/createTask', {
            title,
            description
          });
          
          console.log(res);
        */
          
        try {
          // Verifica si hay un ID en los parámetros para decidir si crea una tarea o actualiza los datos de la tarea.
          if (!params.id) {
            const res = await createTask({ title, description });
            console.log(res);
          } else {
            const res = await updateTask(params.id, { title, description });
            console.log(res);
          }
          navigate("/");
        } catch (error) {
          console.error(error);
          // Muestra una alerta en caso de error con detalles del servidor
          if (error.response?.data) {
            alert(error.response.data.detail);
          }
        }
        // Restablece el formulario
        e.target.reset();
      };

      // Carga los datos de la tarea si hay un ID en los parámetros
      useEffect(() => {
        if (params.id) {
          // Obtiene los datos de la tarea, como el titulo y discripcion y actualiza los estados locales
          fetchTask(params.id)
            .then((res) => {
              setTitle(res.data.title);
              setDescription(res.data.description);
            })
            .catch((error) => {
              console.error(error);
            });
        }
      }, []);

      
    // Renderiza el formulario y botones de acción
    return(
        <div className="flex items-center justify-center h-[calc(100vh-10rem)]">
            <div>
                <form className="bg-zinc-950 bg-opacity-70 p-10" onSubmit={handleSubmit}>
                  <h1 className="text-3xl font-bold my-4">
                    {
                      params.id? "Update Task" : "Create Task"
                    }
                  </h1>
                  <input
                      type="text"
                      placeholder="title"
                      className="block p-2 py-2 px-3 mb-4 w-full text-black"
                      onChange={(e) => setTitle(e.target.value)}
                      value={title}
                      autoFocus
                  />
                  <textarea
                      placeholder="description"
                      className="block p-2 py-2 px-3 mb-4 w-full text-black"
                      onChange={(e) => setDescription(e.target.value)}
                      value={description}
                  ></textarea>
                  <button className="bg-white hover:bg-slate-800 hover:text-white text-slate-800 font-bold bg-opacity-70 py-2 px-4 rounded">
                      {params.id ? "Update" : "Create"}
                  </button>
                </form>

                {params.id && (
                <button
                    className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 rounded mt-5"
                    onClick={async () => {
                    try {
                        const res = await deleteTask(params.id);
                        console.log(res);
                        navigate("/");
                    } catch (error) {
                        console.error(error);
                    }
                    }}
                >
                    Delete
                </button>
                )}
            </div>
        </div>
    );
}

export default TaskForm