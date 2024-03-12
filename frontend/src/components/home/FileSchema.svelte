<script lang="ts">
	import type { TableSchema } from '../../backend/interfaces/files/files.ts';

	export let schema: TableSchema
	export let tableName: string | null

	export let closePopup: () => void;
</script>

<div class="popup-background">
	<div class="main-container-schema">
		<div class="container-schema-header">
		<h1>{tableName}</h1>
			<div aria-hidden="true" class="close-button" on:click={closePopup}>
				<i class="fa-solid fa-x"></i>
			</div>
		</div>
		{#if schema}
			{#each schema.schema as column}
				<div class="column-container">
					<div class="column-apresentation">
						<p class="column-desc">Nome da coluna</p>
						<p class="column-value">{column.column_name}</p>
					</div>
					<div>
						<p class="column-desc">Tipo de coluna</p>
						<p class="column-value">{column.column_type}</p>
					</div>
					<div class="column-apresentation change-type-column">
						<label class="column-desc">Alterar tipo</label>
						<select class="select-type">
							<option>BIGINT</option>
							<option>VARCHAR</option>
							<option>DATE</option>
							<option>BOOL</option>
							<option>NUMERIC</option>
						</select>
					</div>
				</div>
			{/each}
		{/if}
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

    .main-container-schema {
				display: flex;
				flex-direction: column;
        width: 30%;
        border-radius: 10px;
        background-color: white;
        color: black;
        padding: 20px;
    }

    .container-schema-header {
        display: flex;
        justify-content: space-between;
    }

    .close-button {
        cursor: pointer;
				font-size: 25px;
				color: red;
    }

		.column-apresentation {
				margin: 0;
		}

		.column-container {
				display: flex;
				flex-direction: row;
				gap: 8%;
				text-align: left;
				font-size: 15px;
				margin: 3%;
		}

		.column-desc {
				font-size: 18px;
				margin: 0;
		}

		.column-value {
				font-size: 18px;
				font-weight: bold;
				margin:0;
		}

		.change-type-column {
				display: flex;
				flex-direction: column;
				margin: auto 0;
				text-align: center;
		}

		.select-type {
				border-radius: 5px;
				padding: 10px;
				font-size: 13px;
				font-weight: bold;
		}
</style>