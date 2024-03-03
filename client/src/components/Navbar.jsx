import { Link, useLocation } from "react-router-dom";

// Defino el componente de barra de navegacion
function Navbar() {
  const location = useLocation();

  return (
    <header className="flex justify-between items-center my-7">
      <Link to="/">
        <h1 className="text-black text-3xl font-bold"> &lt; Task App &gt; </h1>
      </Link>
      {location.pathname === "/" ? (
        <Link
          to="/task/createTask"
          className="bg-blue-700 hover:bg-blue-500 text-white font-bold py-2 px-4 rounded"
        >
          Create Task
        </Link>
      ) : (
        <Link
          to="/"
          className="bg-blue-700 hover:bg-blue-500 text-white font-bold py-2 px-4 rounded"
        >
          Back
        </Link>
      )}
    </header>
  );
}

export default Navbar;