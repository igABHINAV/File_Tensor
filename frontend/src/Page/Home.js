import React, { useState } from 'react'

const Home = () => {
    const [file, setFile] = useState(null);
    const [folder, setfolder] = useState('')
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    }

    const handleUpload = async () => {
        const data = new FormData();
        data.append('files', file);


        const response = await fetch('http://127.0.0.1:8000/api/upload/', {
            method: 'POST',
            body: data
        });
        const aata = await response.json();
        if (response.status === 200) {
            setfolder(aata.data.folder)

        }

    }

    return (
        <div className='container text-center'>
            <div class="mb-3">
                <label for="formFileMultiple" class="form-label">Upload Your file Here !</label>
                <input class="form-control" type="file" id="formFileMultiple" onChange={handleFileChange}  />
            </div>

            <button className='btn btn-primary text-center' onClick={handleUpload}>submit</button>
            <br /><br/><br/>
            <span className='text-center'>copy the link to download(once submitted) :  </span>
            <p style={{"color":"blue"}}> http://127.0.0.1:8000/media/zipfiles/{folder}.zip</p>
        </div>
    )
}

export default Home
