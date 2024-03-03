import axios from "axios";

const URL = import.meta.env.VITE_API;
const endpoint = URL + "/task";

export const fetchTasks = () => axios.get(`${endpoint}/tasks`);

export const fetchTask = (id) => axios.get(`${endpoint}/getTask/${id}`);

export const createTask = (task) => axios.post(`${endpoint}/createTask`, task);

export const updateTask = (id, task) => axios.put(`${endpoint}/updateTask/${id}`, task);

export const deleteTask = (id) => axios.delete(`${endpoint}/deleteTask/${id}`);