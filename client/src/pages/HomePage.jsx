import { useEffect, useState } from "react"
// import axios from "axios"
import TaskList from '../components/TaskList'
import { fetchTasks } from "../../api/tasks";

function HomePage(){
    const [completedTasks, setCompletedTasks] = useState([]);
    const [pendingTasks, setPendingTasks] = useState([]);
  

    // const [tasks, setTasks] = useState([]);

    // useEffect(() => {
    //     async function fetchTasks(){
    //         const res = await axios.get('http://localhost:8000/task/tasks')
    //         console.log(res)
    //     }
    //     fetchTasks();
    // }, []);

    useEffect(() => {
        fetchTasks()
          .then((res) => {
            setCompletedTasks(res.data.filter((task) => task.completed));
            setPendingTasks(res.data.filter((task) => !task.completed));
          })
          .catch((err) => console.log(err));
      }, []);

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


        <h3 className="text-xl font-bold text-gray-400 mb-7">Pending Tasks</h3>
        <TaskList tasks={pendingTasks} />

        <h3 className="text-xl font-bold text-gray-400 mb-7">Completed Task</h3>
        <TaskList tasks={completedTasks} />

        </>
    )
}

export default HomePage