import { useEffect, useState } from "react"
// import axios from "axios"
import TaskList from '../components/TaskList'
import { fetchTasks } from "../../api/tasks";

// Pagina principal, muestro tareas pedientes y completadas //
function HomePage(){
    const [completedTasks, setCompletedTasks] = useState([]);
    const [pendingTasks, setPendingTasks] = useState([]);
  
    /*
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        async function fetchTasks(){
            const res = await axios.get('http://localhost:8000/task/tasks')
            console.log(res)
        }
        fetchTasks();
    }, []);
    */

    useEffect(() => {
        // Llama a la función para obtener todas las tareas
        fetchTasks()
          .then((res) => {
            // Filtra las tareas completadas y pendientes
            setCompletedTasks(res.data.filter((task) => task.completed));
            setPendingTasks(res.data.filter((task) => !task.completed));
          })
          .catch((err) => console.log(err));
      }, []);  // El array vacío como segundo argumento significa que este efecto se ejecuta solo al incializar el componente

    return(
        <>
        {/* <h1 className="text-3xl font-bold">HomePage</h1>

        <TaskList tasks={tasks}/> */}
        
        {/* {
            tasks.map(task => (
                <div>
                    <h2>{task.title}</h2>
                    <p> {task.description} </p>
                </div>
            ))
        } */}


        <h3 className="text-xl font-bold bg-orange-300 text-black pl-4 mb-3 rounded">Pending Tasks</h3>
        <TaskList tasks={pendingTasks} />

        <h3 className="text-xl font-bold bg-green-300 text-black pl-4 mt-10 mb-3 rounded">Completed Task</h3>
        <TaskList tasks={completedTasks} />

        </>
    )
}

export default HomePage