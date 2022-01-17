import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import Login from './views/auth/Login'; 
import Signup from './views/auth/Signup'; 
import Logout from './views/auth/Logout'; 
import Dashboard from './app/Dashboard';
import ChatHistory from './app/ChatHistory';

const App = () => {
  return (
    <div className='App'>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/login' element={<Login/>} />
          <Route path='/signup' element={<Signup/>} />
          <Route path='/logout' element={<Logout/>} />
          <Route path='/dashboard' element={<Dashboard/>} />
          <Route path='/chatHistory' element={<ChatHistory/>} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;