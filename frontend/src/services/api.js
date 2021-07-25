import axios from 'axios';

async function post(url, payload, options={}) {
    return axios.post(url, payload, options)
}

export { post };
