import { apiPath } from '../../main';
import type { Files, TableSchema } from '../../interfaces/files/files';

export async function getAllFiles():Promise<Files|null> {
	console.log("TRY REQUEST")
	const request = await fetch(`${apiPath}/file/list`, {
		method:"GET"
	})

	const response = await request.json()
	console.log(response)

	if (request.status == 200) {
		return response as Files
	}

	console.log("DEU")
	return null
}

export async function getSchema(id_table:number):Promise<TableSchema|null> {
	const request = await fetch(`${apiPath}/file/schema?id=${id_table}`, {
		method:"GET"
	})

	const response = await request.json()

	if (request.status == 200) {
		return response as TableSchema
	}

	return null
}
