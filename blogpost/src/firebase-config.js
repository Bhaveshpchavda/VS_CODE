// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getAuth , GoogleAuthProvider} from 'firebase/auth';
import {getFirestore} from'firebase/firestore';
 
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBNoCgLHXHhZoaMlvWLBbWoDGZCuUcA68k",
  authDomain: "blogpost-4b62a.firebaseapp.com",
  projectId: "blogpost-4b62a",
  storageBucket: "blogpost-4b62a.appspot.com",
  messagingSenderId: "97077877359",
  appId: "1:97077877359:web:ae80b39a588efdf4eacb9a",
  measurementId: "G-3WTD552ZWC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const db = getFirestore(app);
export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();



