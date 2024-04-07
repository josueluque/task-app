import fs from "fs";

const envVariables = {
    VITE_API: 'http://localhost:8000',

};

const envContent = Object.entries(envVariables)
  .map(([key, value]) => `${key}=${value}`)
  .join("\n");

const envFilePath = ".env";

fs.writeFileSync(envFilePath, envContent);

console.log(`Archivo ${envFilePath} generado con éxito.`);