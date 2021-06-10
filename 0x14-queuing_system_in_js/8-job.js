const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
      throw (new Error('Jobs is not an array'));
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if( !err ) console.log("Notification job created:", job.id );
         });
      job.on('complete', () => console.log(`Notification job ${job.id} completed`));
      job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
      job.on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
  }
  
  module.exports = createPushNotificationsJobs;