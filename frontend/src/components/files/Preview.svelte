<script lang="ts">

	import type { DynamicRow } from '../../backend/interfaces/files/row_preview.ts';

	export let rowsPreview: DynamicRow | null = null

</script>

{#if rowsPreview}
	<div class="table-preview-container">
		<div class="table-preview">
			<table>
				<thead>
				<tr>
					{#each Object.keys(rowsPreview[0]) as key}
						<th>{key}</th>
					{/each}
				</tr>
				</thead>
				<tbody>
				{#each rowsPreview as row}
					<tr>
						{#each Object.values(row) as value}
							<td>{value}</td>
						{/each}
					</tr>
				{/each}
				</tbody>
			</table>
		</div>
	</div>
{/if}

<style>
		.table-preview-container {
        display: flex;
        flex-direction: column;
        width: 35%;
				max-height: 50vh;
				max-width: 40%;
				overflow-y: auto;
				overflow-x: auto;
        background-color: #fafafa;
        border-radius: 7px;
        box-shadow: 5px 15px 25px rgba(17, 17, 17, 0.2);
				margin: 0 0 0 5%;
		}

		.table-preview {
			margin: 5%;
		}

    table {
        border-collapse: collapse;
        width: 100%;
				border-radius: 5px;
    }

    th, td {
        border: 1px solid grey;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }
</style>