import { useState } from 'react'


export default function FileSummary() {
  const [file, setFile] = useState(null);
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    fetch('/upload', {
      method: 'POST',
      body: formData
    }).then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Network response was not ok.');
    }).then((data) => {
      const textSummary = data.textSummary;
      const brailleSummary = data.brailleSummary;
      const readAloudSummary = data.readAloudSummary;

      // Update the content of the summary elements
      document.getElementById('text-summary').textContent = textSummary;
      document.getElementById('braille-summary').textContent = brailleSummary;
      document.getElementById('read-aloud-summary').textContent = readAloudSummary;

    }).catch((error) => {
      console.error('There was a problem with the network request:', error);
    });
  };

  return (
    <div>
      <div className='flex flex-col justify-center items-center m-16 p-12 '>
        <p className='font-bold m-12 text-6xl text-center'>Generate Summary Of A File</p>
        <input onChange={handleFileChange} type="file" id="helper-text" aria-describedby="helper-text-explanation" className="w-1/2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-4  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  mt-12" placeholder="Select the file of which you want summary" />
        <button onClick={handleSubmit} className='flex justify-center items-center h-16 w-64 text-2xl rounded-2xl border-solid border-2 border-black bg-white mt-16 text-black'>GENERATE</button>
      </div>
      <div id="text-summary"></div>
      <div id="braille-summary"></div>
      <div id="read-aloud-summary"></div>

      <div id="second" className="flex flex-col justify-center items-center m-16 mb-64 mt-64 p-12">
        <p className="font-bold m-12 text-6xl text-center">In Which Way You Want Summary ? </p>
        <div className="flex flex-row justify-center items-center">
          <button className='h-16 w-64 text-2xl rounded-2xl border-solid border-2 border-black bg-white mt-16 text-black'>Textual Summary</button>
          <button className='h-16 w-64 text-2xl rounded-2xl border-solid border-2 border-black bg-white mt-16 text-black  ml-12'>Audio Summary</button>
          <button className='h-16 w-64 text-2xl rounded-2xl border-solid border-2 border-black bg-white mt-16 text-black ml-12'>Braille Text Summary</button>
        </div>
      </div>

    </div>
  )
}


