import {BrowserRouter, Route, Routes} from 'react-router-dom'
import HomePage from './pages/HomePage'
import TaskForm from './pages/TaskForm'
import Navbar from './components/Navbar'


function App(){
  return(
    <BrowserRouter>
      {/* Contenedor principal con estilos de tailwind */}
      <div className='container mx-auto px-4'>

        {/* Barra de navegación */}
        <Navbar/>

        {/* Configuración de rutas */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/task/:id" element={<TaskForm />} />
          <Route path="/task/createTask" element={<TaskForm />} />
        </Routes>  
           
      </div>
    </BrowserRouter>
  )
}

export default App