import kue from 'kue';

const Q = kue.createQueue();
const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (!blacklist.includes(phoneNumber)) {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    done();
  } else {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }
}

Q.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
