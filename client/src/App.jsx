import {BrowserRouter, Route, Routes} from 'react-router-dom'
import HomePage from './pages/HomePage'
import TaskForm from './pages/TaskForm'

function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/tasks/:id" element={<TaskForm />} />
        <Route path="/tasks/new" element={<TaskForm />} />
      </Routes>     
    </BrowserRouter>
  )
}

export default App