<script lang="ts">
	import { sendFile, tablePreview } from '../../backend/requests/file/post.ts';
	import type { DynamicRow } from '../../backend/interfaces/files/row_preview.ts';
	import Preview from '../files/Preview.svelte';
	export let closePopup: () => void;

	let isCsvFile = false
	let isValidFile = false
	let fileSeparator: string = ','
	let tableDemonstration: DynamicRow | null = null
	let showPreview = false
	let haveHeader = false

	function handleCheckboxChange(event: Event) {
		haveHeader = event.target.checked;
	}

	function checkFileExtension(event: Event) {

		const uploadedFile = (event.target as HTMLInputElement).files[0]
		if (uploadedFile) {
			const fileExtension = uploadedFile.name.split(".")[uploadedFile.name.split(".").length - 1]
			isValidFile = true

			if (fileExtension === 'csv') {
				isCsvFile = true
			}
		}
	}

	async function sendFileEvent(event: Event) {
		event.preventDefault();

		const uploadedFile = document.getElementById('csv-file').files[0];

		const request = await sendFile(uploadedFile, fileSeparator, haveHeader)

		console.log(request)
	}


	async function generatePreview(event: Event) {
		event.preventDefault();

		if (showPreview) {
			showPreview = false
		} else {
			tableDemonstration = null
			const uploadedFile = document.getElementById('csv-file').files[0];
			tableDemonstration = await tablePreview(uploadedFile, fileSeparator, haveHeader)
			showPreview = true
		}
	}

</script>
<div class="popup-background">
	<div class="main-container-input-file">
		<div class="container-schema-header">
			<h3 class="title-header">Selecione um arquivo .parquet ou .csv</h3>
			<div aria-hidden="true" class="close-button" on:click={closePopup}>
				<i class="fa-solid fa-x"></i>
			</div>
		</div>
		<div class="input-file-container">
			<div class="input-file">
				<label on:change={checkFileExtension} for="images" class="drop-container" id="dropcontainer">
					<span class="drop-title">Drop files here</span>
					or
					<input type="file" id="csv-file" accept=".csv" required>
				</label>
			</div>
			{#if isCsvFile}
			<div class="input-file-separator">
				<label>Separator:
					<select bind:value={fileSeparator}>
						<option value=",">,</option>
						<option value=";">;</option>
						<option value="tab">Tab (4 spaces)</option>
					</select>
				</label>
				<div class="input-file-header">
					<label for="header">First row as column:</label>
					<input class="row-header" on:change={handleCheckboxChange} id="header" type="checkbox">
				</div>
			</div>
			{/if}
			<div class="actions-container">
				<div class="send-file-container">
					<button
						class:send-file={isValidFile}
						class:send-file-disabled={!isValidFile}
						on:click={sendFileEvent}
						disabled={!isValidFile}>
						Send
					</button>
				</div>
				<div class="generate-preview-container">
					<button
						class:generate-preview={isValidFile}
						on:click={generatePreview}
						class:generate-preview-disabled={!isValidFile}
						class:deactive-preview={showPreview}
						disabled={!isValidFile}>
						Generate preview
					</button>
				</div>
			</div>
		</div>
	</div>
	{#if tableDemonstration && showPreview}
		<Preview rowsPreview={tableDemonstration}/>
	{/if}
</div>

<style>
    .popup-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
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
        max-height: 90vh;
        max-width: 800px;
        overflow-x: auto;
        overflow-y: auto;
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
        font-size: 30px;
        color: grey;
				margin: 1% 5% 0 0;
				transition: 0.3s ease;
    }

		.close-button:hover {
				transform: scale(1.1);
				color: red;
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

		.input-file-separator {
				margin: 5% auto 3% auto;
				font-size: 15px;
		}

		.input-file-header {
				display: flex;
				justify-content: center;
				text-align: center;
				align-items: center;
		}

    input[type="checkbox"] {
        width: 20px;
        height: 15px;
        background: transparent;
        border-radius: 50px;
		}

		.input-file-separator label {
				font-size: 13px;
		}

		.input-file-separator select {
				border-radius: 5px;
				padding: 10px;
				font-size: 10px;
		}

		.actions-container {
				display: flex;
				flex-direction: row;
		}

		.send-file-container, .generate-preview-container {
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

    .generate-preview {
        padding: 15px 20px;
        border-radius: 5px;
        border: none;
        margin: 20% auto;
        background-color: #039b1c;
        color: white;
        transition: 0.5s ease;
    }

		.deactive-preview {
        padding: 15px 20px;
        border-radius: 5px;
        border: none;
        margin: 20% auto;
        background-color: #911111;
        color: white;
        transition: 0.5s ease;
		}

		.generate-preview-disabled, .send-file-disabled {
				color: black;
        border-radius: 5px;
        border: none;
        margin: 20% auto;
        background-color: #b9b9b9;
        transition: 0.5s ease;
		}

		.generate-preview-disabled {
        padding: 15px 20px;
		}

		.send-file-disabled {
        padding: 15px 50px;
		}

		.send-file:hover, .generate-preview:hover {
				transform: scale(1.05);
		}
</style>