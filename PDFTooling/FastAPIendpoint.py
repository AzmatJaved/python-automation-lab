@router.post("/merge")
async def merge(
    files: list[UploadFile],
    background_tasks: BackgroundTasks,
    user: User = Depends(get_current_user)
):
    check_usage_limit(user)  # enforce free tier limits
    job_id = create_job(user.id, "merge")
    background_tasks.add_task(process_merge, job_id, files)
    return {"job_id": job_id, "status": "processing"}

@router.get("/job/{job_id}")
async def get_job_status(job_id: str):
    job = get_job(job_id)
    return {"status": job.status, "download_url": job.download_url}