<script lang="ts">
	import type { Files, TableSchema } from '../../backend/interfaces/files/files.ts';
	import { getSchema } from '../../backend/requests/file/get.ts';
	import FileSchema from './FileSchema.svelte';
	import InputFile from './InputFile.svelte';
	export let listOfFiles: Files | null
	let popUpFileSchema: boolean = false
	let popUpFileInput: boolean = false
	let schemaFile: null | TableSchema = null
	let tableName: null | string = null

	async function showPopUpSchema(id_table:number, table_name:string) {
		schemaFile = await getSchema(id_table)
		if (schemaFile) {
			tableName = table_name
			popUpFileSchema = true
		}
	}

	function closeFileSchemaPopup() {
		popUpFileSchema = false;
	}

	function openFileInputPop() {
		popUpFileInput = true
	}

	function closeFileInputPop() {
		popUpFileInput = false
	}
</script>
{#if popUpFileInput}
	<InputFile closePopup={closeFileInputPop}/>
{/if}
{#if popUpFileSchema && schemaFile}
	<FileSchema schema={schemaFile} tableName={tableName} closePopup={closeFileSchemaPopup}/>
{/if}
<div class="metadata-container">
	<div class="header-metadata-container">
		<h1 class="title-header">File management.</h1>
		<div aria-hidden="true" on:click={openFileInputPop} class="add-file-container">
			<p class="label-add-file">Add file</p>
			<i class="fa-solid fa-plus add-file"></i>
		</div>
	</div>
	<div class="container-files-metadata">
			{#if listOfFiles}
				{#each listOfFiles.files as file}
						<div aria-hidden="true" on:click={() => showPopUpSchema(file.id, `${file.name}.${file.type}`)} class="file-container">
							<div class="name-file">
								<p class="file-value-desc">Nome do arquivo</p>
								<div class="container-file-value">
									<i class="fa-solid fa-file value-icon"></i>
									<p class="file-value">{file.name}</p>
								</div>
							</div>
							<div class="size-file">
								<p class="file-value-desc">Tamanho do arquivo (MB)</p>
								<div class="container-file-value">
									<i class="fa-solid fa-floppy-disk value-icon"></i>
									<p class="file-value">{file.size}</p>
								</div>
							</div>
							<div class="columns-file">
								<p class="file-value-desc">Quantidade de colunas</p>
								<div class="container-file-value">
									<i class="fa-solid fa-chart-column value-icon"></i>
									<p class="file-value">{file.nb_columns}</p>
								</div>
							</div>
							<div class="rows-file">
								<p class="file-value-desc">Quantidade de linhas</p>
								<div class="container-file-value">
									<i class="fa-solid fa-chart-simple value-icon"></i>
									<p class="file-value">{file.nb_rows}</p>
								</div>
							</div>
						</div>
				{/each}
			{/if}
	</div>
</div>

<style>
	.metadata-container {
			width: 50%;
			margin: 5% auto 5% 15%;
			max-height: 80vh;
			overflow-y: auto;
			height: auto;
			border-radius: 10px;
      box-shadow: 5px 15px 25px rgba(17, 17, 17, 0.2);
			background-color: #fdfdfd;
	}

	.header-metadata-container {
			display: flex;
			flex-direction: row;
			justify-content: space-between;
	}

	.title-header {
			margin: auto auto auto 5%;
	}

	.add-file-container {
			display: flex;
			justify-content: right;
			background-color: #0d45a5;
			width: 20%;
			border-radius: 10px;
			transition: 0.5s ease;
			margin: 3%;
			color: white;
			cursor: pointer;
			padding: 10px 0;
	}

	.add-file {
			font-size: 30px;
			margin: auto 5% auto 5%;
	}

	.label-add-file {
			margin: auto;
	}

	.add-file-container:hover {
			color: white;
			transform: scale(1.1);
	}

  .container-files-metadata {
      display: flex;
      flex-direction: column;
			padding: 20px;
  }

  .file-container {
			cursor: pointer;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      margin: 2%;
			border-radius: 10px;
			padding: 10px;
  }

	.file-container:hover {
			background-color: #1F2937;
	}

  .file-container:hover .file-value,
  .file-container:hover .file-value-desc,
	.file-container:hover .value-icon
	{
      color: white;
  }

	.file-value-desc {
			text-align: left;
			font-weight: bold;
			font-size: 15px;
			margin: 0;
	}

	.container-file-value {
			display: flex;
			flex-direction: row;
	}

	.value-icon {
			margin: auto 5%;
			font-size: 20px;
	}

	.file-value {
			text-align: center;
			font-size: 18px;
	}

</style>