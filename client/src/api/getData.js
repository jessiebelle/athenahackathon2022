import axios from 'axios';
import DATA from '../userData';


const getData = async () => {
  try {
    let response = await axios.get(DATA);
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export default getData;
