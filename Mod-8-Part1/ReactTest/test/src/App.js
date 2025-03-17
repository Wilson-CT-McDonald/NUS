import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BootButton, WelcomeMessage } from './welcomeMessage';
import BootModal from './BootModal';

function App() {
  return (
    <div className='App'>
      <WelcomeMessage name="Wilson" />
      <BootButton color="primary" name="click me" />
      <BootModal 
        color1 = "primary"
        name1 = "Click me!!!"
        color2 = "success"
        name2 = "Do you agree?"
        color3 = "secondary"
        name3 = "Cancel" 
        mbody = "here are T&C"       
      />
    </div>
  );
}

export default App;
