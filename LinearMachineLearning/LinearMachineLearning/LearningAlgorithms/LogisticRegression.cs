using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinearMachineLearning.DataHandling;

namespace LinearMachineLearning.LearningAlgorithms
{
    public class LogisticRegression : LinearModel
    {
        #region Parameters
        public double[] ErrorGradient { get; set; }
        public double LearningRate { get; set; }
        public double MaxError { get; set; }
        public int MaxItterations { get; set; }
        #endregion

        #region Constructors
        public LogisticRegression()
        {
            InputSize = 1;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            ErrorGradient = new double[InputSize];
            Output = 0;
            InSampleError = 0;
            MaxError = .1;
            LearningRate = .1;
            MaxItterations = 10000;
        }
        public LogisticRegression(int inputSize)
        {
            InputSize = inputSize;
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            ErrorGradient = new double[InputSize];
            Output = 0;
            InSampleError = 0;
            MaxError = .1;
            LearningRate = .1;
            MaxItterations = 10000;
        }
        public LogisticRegression(string filePath)
        {
            FilePath = filePath;
            string[] lines = System.IO.File.ReadAllLines(filePath);

            Name = lines[0];
            InputSize = Convert.ToInt32(lines[1]);
            Inputs = new double[InputSize];
            Weights = new double[InputSize];
            ErrorGradient = new double[InputSize];

            string[] stringWeights = lines[2].Split(',');
            for (int index = 0; index < stringWeights.Length; index++)
            {
                Weights[index] = Convert.ToDouble(stringWeights[index]);
            }

            InSampleError = 0;
            MaxError = .1;
            Output = 0;
            LearningRate = .1;
            MaxItterations = 10000;
        }
        #endregion

        #region Methods
        public override void ComputeOutput(double[] input)
        {
            base.ComputeOutput(input);
            Output = 1 / (1 + Math.Exp(-1 * Output));
        }

        public override double ComputeSinglePointError(DataPoint point)
        {
            ComputeOutput(point.Input);
            double e = Math.Log(1 + Math.Exp(-1 * point.Output * Output));
            return e;
        }

        public override void ComputeInSampleError(DataSet set)
        {
            InSampleError = 0;
            foreach(DataPoint point in set.Examples)
            {
                InSampleError += ComputeSinglePointError(point);
            }
            InSampleError /= set.NumberExamples;
        }

        public void ComputeErrorGradient(DataSet set)
        {
            //Reset Error gradient to zeros
            for(int gradIndex = 0; gradIndex < ErrorGradient.Length; gradIndex++)
            {
                ErrorGradient[gradIndex] = 0;
            }

            //Handles the main sum of the equation
            foreach(DataPoint point in set.Examples)
            {
                double baseOut = base.ComputeAndReturnOutput(point.Input);
                for (int gradIndex = 0; gradIndex < ErrorGradient.Length; gradIndex++)
                {
                    ErrorGradient[gradIndex] += (point.Output * point.Input[gradIndex]) / (1 + Math.Exp( point.Output * baseOut ) );
                }
            }

            //Divides ErrorGradient by number of examples
            for(int gradIndex = 0; gradIndex < ErrorGradient.Length; gradIndex++)
            {
                ErrorGradient[gradIndex] /= (-1 * set.NumberExamples);
            }
        }

        public override void Learn(DataSet set)
        {
            ComputeInSampleError(set);
            int itteration = 0;
            while(InSampleError > MaxError)
            {
                //Getting the current error gradient
                ComputeErrorGradient(set);

                //Updating each weight
                for(int weightIndex = 0; weightIndex < InputSize; weightIndex++)
                {
                    Weights[weightIndex] = Weights[weightIndex] - LearningRate * ErrorGradient[weightIndex];
                }

                //Checking whether to stop or not
                ComputeInSampleError(set);
                itteration++;
                if(itteration > MaxItterations)
                {
                    break;
                }
            }
        }
        #endregion
    }
}
