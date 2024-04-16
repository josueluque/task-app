import axios from "./axios";

export const fetchTasks = () => axios.get(`task/tasks`);

export const fetchTask = (id) => axios.get(`task/getTask/${id}`);

export const createTask = (task) => axios.post(`task/createTask`, task);

export const updateTask = (id, task) => axios.put(`task/updateTask/${id}`, task);

export const deleteTask = (id) => axios.delete(`task/deleteTask/${id}`);    