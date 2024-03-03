import TaskCard from "./TaskCard";

// Defino el componente lista de tareas
function TaskList({ tasks }) {
  return (
    <div className="grid grid-cols-4 gap-4 ">

      {/* Mapea sobre el arreglo de tareas y renderiza un componente TaskCard para cada tarea */}
      {tasks.map((task, i) => {
        return <TaskCard task={task} key={i} />;
      })}
    </div>
  );
}

export default TaskList;