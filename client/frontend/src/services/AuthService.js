const API_URL = "http://127.0.0.1:8000/login";

import { removeItem } from "./LocalStorageService";

export const login = (credientials, callback) => {
    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(credientials),
    })
        .then((res) => res.json())
        .then((res) => { 
            callback(res);
        });
} 

export const logout = () => {
    removeItem("_token");
}
