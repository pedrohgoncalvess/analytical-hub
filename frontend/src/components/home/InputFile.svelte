<script lang="ts">
	import axios from 'axios';
	export let closePopup: () => void;

	async function enviarArquivo(event) {
		event.preventDefault();

		const formData = new FormData();
		formData.append('file', event.target.csvFile.files[0]);

		try {
			const response = await axios.post('http://localhost:9000/upload/file?separator=%3B', formData, {
				headers: {
					'Content-Type': 'multipart/form-data',
				},
			});

			console.log(response.data);
		} catch (error) {
			console.error('Erro ao enviar arquivo:', error);
		}
	}
</script>
<div class="popup-background">
	<div class="main-container-input-file">
		<div class="container-schema-header">
			<h2 class="title-header">Selecione um arquivo</h2>
			<div aria-hidden="true" class="close-button" on:click={closePopup}>
				<i class="fa-solid fa-x"></i>
			</div>
		</div>
		<form class="input-file-container" on:submit={enviarArquivo}>
			<div class="input-file">
				<label for="images" class="drop-container" id="dropcontainer">
					<span class="drop-title">Drop files here</span>
					or
					<input type="file" id="images" accept=".csv" required>
				</label>
			</div>
			<div class="send-file-container">
				<button class="send-file" type="submit">Enviar</button>
			</div>
		</form>
	</div>
</div>

<style>
    .popup-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

		.main-container-input-file {
				display: flex;
				flex-direction: column;
				width: 30%;
        background-color: #fafafa;
				border-radius: 7px;
        box-shadow: 5px 15px 25px rgba(17, 17, 17, 0.2);
		}

    .container-schema-header {
        display: flex;
        justify-content: space-between;
				height: max-content;
    }

		.title-header {
				text-align: center;
				margin: auto;
		}

    .close-button {
        cursor: pointer;
        font-size: 35px;
        color: red;
				margin: 1% 5% 0 0;
    }

		.input-file-container {
				display: flex;
				flex-direction: column;
				margin: 10% auto;
				justify-items: center;
		}

		.input-file {
				margin: auto;
				text-align: center;
		}

    input[type=file]::file-selector-button {
        margin-right: 20px;
        border: none;
        background: #084cdf;
        padding: 10px 20px;
        border-radius: 10px;
        color: #fff;
        cursor: pointer;
        transition: background .2s ease-in-out;
    }

    input[type=file]::file-selector-button:hover {
        background: #0d45a5;
    }

    .drop-container {
        position: relative;
        display: flex;
        gap: 10px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 200px;
        padding: 30px;
        border-radius: 10px;
        border: 2px dashed #555;
        color: #444;
        cursor: pointer;
        transition: background .2s ease-in-out, border .2s ease-in-out;
    }

    .drop-container:hover {
        background: #eee;
        border-color: #111;
    }

    .drop-container:hover .drop-title {
        color: #222;
    }

    .drop-title {
        color: #444;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        transition: color .2s ease-in-out;
    }

		.send-file-container {
				margin: auto;
		}

		.send-file {
				padding: 15px 50px;
				border-radius: 5px;
				border: none;
				margin: 20% auto;
				background-color: #0d45a5;
				color: white;
				transition: 0.5s ease;
		}

		.send-file:hover {
				transform: scale(1.2);
		}
</style>